#version 150

#moj_import <minecraft:fog.glsl>
#moj_import <minecraft:dynamictransforms.glsl>
#moj_import <minecraft:projection.glsl>
#moj_import <minecraft:globals.glsl>
#moj_import <minecraft:light.glsl>
#moj_import <vsh_util.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV2;

uniform sampler2D Sampler0;
uniform sampler2D Sampler2;

out float sphericalVertexDistance;
out float cylindricalVertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;

void main() {
	vec3 offsetPosition = Position;
	vec4 finalColor = Color;
	ivec3 colorCheck = ivec3(Color.rgb * 255);
	// buff disappearing flash
	if (colorCheck == ivec3(255, 255, 251))
	{
		float alpha = (10.0 - mod(GameTime * 24000, 10.0)) / 10.0;
		finalColor = vec4(1, 1, 1, alpha * 0.82);
	}
	else if (colorCheck == ivec3(255, 255, 250))  // buff default color
		finalColor = vec4(1, 1, 1, 0.82);
	else if (colorCheck == ivec3(255, 255, 249))  // anti-shadow default color
		finalColor = vec4(1);
	
	// up lift
	ivec4 vertexTexel = ivec4(texture(Sampler0, UV0) * 255);
	if (vertexTexel.rgb == ivec3(1,3,5)) {
		mat3 WorldMat = getWorldMat(Light0_Direction, Light1_Direction);
		// value : height == 1 : 0.1
		if (vertexTexel.a == 255) {  // head hp bar offset
			offsetPosition += WorldMat * vec3(0.0, Color.b * 25.5, 0.0) - vec3(0.0, 0.25, 0.0);
			finalColor = vec4(1.0);
		}
		else if (vertexTexel.a == 1) {  // text_display offset
			offsetPosition += WorldMat * vec3(0.0, Color.a * 25.5, 0.0) - vec3(0.0, 0.25, 0.0);
			finalColor = vec4(1.0, 1.0, 1.0, Color.b);
		}
	}
	// damage number float and fade out
	else if (vertexTexel == ivec4(1,2,3,3)) {
		mat3 WorldMat = getWorldMat(Light0_Direction, Light1_Direction);
		
		// 0 ~ 3 are considered 255 (I don't know why), so values are added by 4 in game
		float tickOffset = Color.a * 255 - 4;
		float tick = mod(mod(GameTime * 24000, 22.0) + 22.0 - tickOffset, 22.0);
		// 0.025 block per tick
		if (tick >= 2.0)
			offsetPosition += WorldMat * vec3(0.0, (tick - 2.0) * 0.025, 0.0) - vec3(0.0, 0.25, 0.0);
		
		if (tick < 2.0 || tick > 20.0)
			finalColor = vec4(0.0);
		else if (tick > 7.0)
			finalColor = vec4(1.0, 1.0, 1.0, (20.0 - tick) / 13.0);
		else
			finalColor = vec4(1.0);
	}
	
	gl_Position = ProjMat * ModelViewMat * vec4(offsetPosition, 1.0);

    sphericalVertexDistance = fog_spherical_distance(offsetPosition);
    cylindricalVertexDistance = fog_cylindrical_distance(offsetPosition);
    vertexColor = finalColor * texture(Sampler2, vec2(UV2 / 16) / textureSize(Sampler2, 0));
    texCoord0 = UV0;
}