#version 150

#moj_import <light.glsl>
#moj_import <fog.glsl>
#moj_import <vsh_util.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV2;
in vec3 Normal;

uniform sampler2D Sampler0;
uniform sampler2D Sampler2;

uniform float FogStart;
uniform int FogShape;
uniform mat4 ModelViewMat;
uniform mat4 ProjMat;
uniform mat3 IViewRotMat;
uniform float GameTime;

uniform vec3 Light0_Direction;
uniform vec3 Light1_Direction;

out float vertexDistance;
out vec4 vertexColor;
out vec4 lightColor;
out vec4 overlayColor;
out vec2 texCoord;
out vec2 texCoord2;
out vec3 Pos;
out float transition;
out float alpha;

flat out int isCustom;
flat out int isGUI;
flat out int isHand;
flat out int noshadow;

#moj_import <objmc_tools.glsl>

void main() {
	mat4 FixProjMat = fixProjMat(ProjMat);
	
    Pos = Position;
    texCoord = UV0;
    overlayColor = vec4(1);
    lightColor = minecraft_sample_lightmap(Sampler2, UV2);
    vec3 normal = (FixProjMat * ModelViewMat * vec4(Normal, 0.0)).rgb;
	
	// alpha fade in
	if (int(Color.r) == 0 && int(Color.g) == 0 && Color.b < 0.4) {  // pure blue color < 0.4 was not used in any cases
		vertexColor = minecraft_mix_light(Light0_Direction, Light1_Direction, Normal, vec4(1));
		alpha = Color.b / 0.39215; // 100.0 / 255
	}
	else {
		vertexColor = minecraft_mix_light(Light0_Direction, Light1_Direction, Normal, Color);
		alpha = -1.0;
	}

    //objmc
    #define ENTITY
    #moj_import <objmc_main.glsl>

    gl_Position = FixProjMat * ModelViewMat * (vec4(Pos, 1.0));
    vertexDistance = fog_distance(ModelViewMat, IViewRotMat * Pos, FogShape);
}