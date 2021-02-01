#version 130

uniform sampler2D DiffuseSampler;
uniform sampler2D ColorSampler;

uniform mat4 ProjMat;
uniform vec2 InSize;
uniform vec2 OutSize;

varying vec2 texCoord;
varying vec2 oneTexel;

float near = 0.01; 
float far  = 100.0;
float LinearizeDepth(float depth) 
{
    float z = depth * 2.0 - 1.0;
    return (near * far) / (far + near - z * (far - near));    
}

void main(){
	vec4 tex_color = texture2D(DiffuseSampler, texCoord);
	if (tex_color.a > 0.9)
	{
		int left_dist = 1;
		while (texture2D(DiffuseSampler, texCoord - vec2(oneTexel.x * left_dist, 0.0)).a > 0.9 && oneTexel.x * left_dist < texCoord.x)
			left_dist = left_dist + 1;
		vec3 target_color_left = texture2D(ColorSampler, texCoord - vec2(oneTexel.x * left_dist, 0.0)).rgb;
		
		int right_dist = 1;
		while (texture2D(DiffuseSampler, texCoord + vec2(oneTexel.x * right_dist, 0.0)).a > 0.9 && oneTexel.x * right_dist < 1.0 - texCoord.x)
			right_dist = right_dist + 1;
		vec3 target_color_right = texture2D(ColorSampler, texCoord + vec2(oneTexel.x * right_dist, 0.0)).rgb;
		
		float total_length = left_dist + right_dist;
		vec3 final_color = target_color_left * (right_dist / total_length) + target_color_right * (left_dist / total_length);
		gl_FragColor = vec4(final_color, 0.75);
	}
	else
		gl_FragColor = tex_color;
}
