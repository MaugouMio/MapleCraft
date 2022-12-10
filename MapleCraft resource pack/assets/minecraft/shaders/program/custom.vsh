#version 150

in vec4 Position;

uniform mat4 ProjMat;
uniform vec2 InSize;
uniform vec2 OutSize;
uniform float Time;
uniform sampler2D VariableSampler;
uniform sampler2D JudgeSampler;

out vec2 texCoord;
out vec2 oneTexel;

#define PI 3.1415926535897932384626433832795

#define VAR_FPS_TEST 0.0
#define VAR_FPS 1.0
#define VAR_SHAKE_FRAME 2.0

int getVar(sampler2D sampler, float id) {
	vec4 var_color = texture(sampler, vec2((id + 0.5) * 0.01, 0.0));
	return int(var_color.r * 255.0)/4*4096 + int(var_color.g * 255.0)/4*64 + int(var_color.b * 255.0)/4;
}

void main(){
    vec4 outPos = ProjMat * vec4(Position.xy, 0.0, 1.0);
	
	// ====================================================
	int fps = getVar(VariableSampler, VAR_FPS) * 5 / 4;
	if (fps == 0)
		fps = 60;
	
	vec2 offset = vec2(0.0, 0.0);
	vec2 scaledPos = outPos.xy;
	int shake_frame = getVar(VariableSampler, VAR_SHAKE_FRAME);
	float anim_time = float(shake_frame) / float(fps);
	if (anim_time > 0.0)
	{
		float r = abs(sin(Time * PI * 8)) * 0.02;
		float theta = fract(sin(Time) * 100000.0) * PI * 2;
		offset = vec2(r * cos(theta), r * sin(theta));
		
		if (anim_time < 1.4)
			scaledPos = outPos.xy * 1.1;
		else
			scaledPos = outPos.xy * (2.5 - anim_time);
	}
	// ====================================================
	
    gl_Position = vec4(scaledPos + offset, 0.2, 1.0);

    oneTexel = 1.0 / InSize;

    texCoord = Position.xy / OutSize;
}
