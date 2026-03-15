#version 150

#moj_import <minecraft:globals.glsl>

uniform sampler2D InSampler;
uniform sampler2D JudgeSampler;

in vec2 texCoord;

out vec4 fragColor;

#define SHAKE_TIME 1.5

#define PI 3.1415926535897932384626433832795

#define VAR_FPS_TEST 0.0
#define VAR_FPS 1.0
#define VAR_SHAKE_FRAME 2.0

int imod(int num, int m) {
	return num - (num / m * m);
}

int getVar(sampler2D sampler, float id) {
	vec4 var_color = texture2D(sampler, vec2((id + 0.5) * 0.01, 0.0));
	return int(var_color.r * 255.0)/4*4096 + int(var_color.g * 255.0)/4*64 + int(var_color.b * 255.0)/4;
}

void setVar(int num, float id) {
	float r = (float(num / 4096) + 0.5) * 4.0 / 255.0;
	num = imod(num, 4096);
	float g = (float(num / 64) + 0.5) * 4.0 / 255.0;
	float b = (float(imod(num, 64)) + 0.5) * 4.0 / 255.0;
	
	if (texCoord.x > id * 0.01 && texCoord.x <= (id + 1) * 0.01)
		fragColor = vec4(r, g, b, 1.0);
}

void copyVar(sampler2D sampler, float fromID, float toID) {
	if (texCoord.x > toID * 0.01 && texCoord.x <= (toID + 1) * 0.01)
		fragColor = texture2D(sampler, vec2((fromID + 0.5) * 0.01, 0.0));
}



void update_fps() {
	float second = mod(GameTime * 1200, 1);
	if (second < 0.1)
		setVar(0, VAR_FPS_TEST);
	else if (second < 0.9)
		setVar(getVar(InSampler, VAR_FPS_TEST) + 1, VAR_FPS_TEST);
	else
		copyVar(InSampler, VAR_FPS_TEST, VAR_FPS);  // record
}

void update_shake(float fps) {
	int nextFrame = getVar(InSampler, VAR_SHAKE_FRAME) + 1;
	if (nextFrame == 1)
		return;
	
	if (nextFrame < SHAKE_TIME * fps)
		setVar(nextFrame, VAR_SHAKE_FRAME);
	else
		setVar(0, VAR_SHAKE_FRAME);
}

void main() {
	vec4 PrevTexel = texture2D(InSampler, texCoord);
	fragColor = PrevTexel;
	
	float fps = getVar(InSampler, VAR_FPS) / 0.8;
	if (fps < 1.0)
		fps = 60.0;
	
	update_fps();
	update_shake(fps);
	
	vec4 judgeTexel = texture2D(JudgeSampler, vec2(0.5, 0.45));
	if (judgeTexel.r > 0.996 && judgeTexel.g < 0.004 && judgeTexel.b < 0.004)
		setVar(1, VAR_SHAKE_FRAME);
}
