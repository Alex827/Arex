#!/usr/bin/bash
#ask for table to populate
echo "Which table to populate?"
read TABLE
#formatting to put into mysql tables
MYSQLOPTS="into table $TABLE fields terminated by ',' lines terminated by '\n' ignore 1 lines (EventCodes, Cruise, @localdate,Local_Time, @localdatetime,GMT_Diff, @gmtdatetime, @lat, @long, DecLat, DecLong, PortObs, StbdObs, @quality, @visib, Precipitation, @CloudPerc, @GlareBearing_L, @GlareBearing_R, @glarequal, @WindDir, @WindSpd, @Bft, @Swell_FT, @SightingNo, InitObserver, @Cue, @ShipHeadingTru, @SightingBearingTru, @BinoReticle, @Distance_M, SightingMethod, @EnvelopeDepth, @EnvelopeDepth2, @EnvelopeWidth, @EnvelopeWidth2, @Best, @Min, @Max, Calf, Species, Species_2, @Sp1_perc, @Sp2_perc, Effort_OnOff, @OffEffortCode, Transect_OnOff, @OffTransectCode, @PrimaryBehavior, OtherBehavior1, OtherBehavior2, Photos, Photographer_Cam1, Camera, @FirstFrame1, @LastFrame1, Photographer_Cam2, Camera_2, @FirstFrame2, @LastFrame2, Comments)  SET Local_Date=str_to_date(@localdate,'%m/%d/%Y'), Local_DateTime=str_to_date(@localdatetime,'%m/%d/%Y %H:%i:%s'), GMT_DateTime=str_to_date(@gmtdatetime,'%m/%d/%Y %H:%i:%s'), Lat=nullif(@lat,''), Longi=nullif(@long,''), Quality=nullif(@quality,''), Visibility=nullif(@visib,''), CloudPerc=nullif(@CloudPerc,''), GlareBearing_L=nullif(@GlareBearing_L,''), GlareBearing_R=nullif(@GlareBearing_R,''), GlareQuality_SL_M_SE=cast(@glarequal as char(3)), WindDir=nullif(@WindDir,''), WindSpd=nullif(@WindSpd,''), Bft=nullif(@Bft,''), Swell_FT=nullif(@Swell_FT,''), SightingNo=nullif(@SightingNo,''), Cue=nullif(@Cue,''), ShipHeadingTru=nullif(@ShipHeadingTru,''), SightingBearingTru=nullif(@SightingBearingTru,''), BinoReticle=nullif(@BinoReticle,''), Distance_M=nullif(@Distance_M,''), EnvelopeDepth=nullif(@EnvelopeDepth,''), EnvelopeDepth2=nullif(@EnvelopeDepth2,''), EnvelopeWidth=nullif(@EnvelopeWidth,''), EnvelopeWidth2=nullif(@EnvelopeWidth2,''), Best=nullif(@Best,''), Min=nullif(@Min,''), Max=nullif(@Max,''), Sp1_perc=nullif(@Sp1_perc,''), Sp2_perc=nullif(@Sp2_perc,''),OffEffortCode=nullif(@OffEffortCode,''), OffTransectCode=nullif(@OffTransectCode,''),PrimaryBehavior=nullif(@PrimaryBehavior,''), FirstFrame1=nullif(@FirstFrame1,''), LastFrame1=nullif(@LastFrame1,''),FirstFrame2=nullif(@FirstFrame2,''), LastFrame2=nullif(@LastFrame2,'')"
DBNAME='calcofi'
#for every csv file
for f in *.csv;
#put it into the specified table
do
	mysql --"execute=load data infile '$PWD/$f' $MYSQLOPTS" $DBNAME 
done
