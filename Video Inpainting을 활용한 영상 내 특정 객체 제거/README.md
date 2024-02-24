# 2023 D&A Conference
**Video Inpainting을 활용한 영상 내 특정 객체 제거**

<br/>

## 1. 배경 & 목적
 
- 기존 Youtube 영상 혹은 TV 프로그램 내 초상권과 관련된 문제 존재
- 동영상 내 주인공을 제외한 나머지 사람들(지정한 사람들)은 모두 inpainting으로 지워지도록 하자

<br/>

## 2. 프로젝트 기간

- 팀 구성 : 2023년 7월 中
- 최종 발표 : 2023년 12월 1일

<br/>

## 3. Model FLow

![image](https://github.com/KiSeoupShin/2023_DNA_Conference/assets/108209592/e4def063-8139-442e-82ca-f89ade17cfb6)


<br/>

전체적인 모델 구조는 다음과 같다.
1. 사용자가 영상과 영상 속 지우고자 하는 객체를 입력
2. YOLO-X를 통해 Frame 별 사람 detection 후 HybridSORT를 통해 Tracking 수행
3. 동시에 PIDNET을 통해 segmentation을 frame 별로 수행
4. 사용자가 지정한 객체의 bounding box와 segmentation 정보를 통해 masking map 생성
5. ProPainter를 통해 Video Inpainting 진행

<br/>

## 4. Model Example

### Input Video
https://github.com/KiSeoupShin/2023_DNA_Conference/assets/108209592/aa05fb07-6837-421b-98d7-d40980778a94

### Output Video
https://github.com/KiSeoupShin/2023_DNA_Conference/assets/108209592/e49254fb-6264-4116-953f-eb99409dad7b


<br/>

## 5. 활용방안
1. 상업적 활용방안
   - 영상 컨텐츠 제작 시, 초상권 문제 해결을 위해 편집 작업에 활용
   - 논란이 된 인물이 등장한 영상에 대해서 간단한 추가 작업을 통해서 문제 해결

2. 개인적인 활용방안
   - 영상 내의 다른 사람을 지워서 추억을 더 아름답게 보관 가능
