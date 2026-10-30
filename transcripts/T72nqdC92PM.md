# From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam

Source: https://www.youtube.com/watch?v=T72nqdC92PM

Uploaded: 2026-09-23

Transcript source: full timestamped publisher transcript at https://ai.engineer/talks/T72nqdC92PM-youtube-4c3b380366d1b7a5121f . Includes slide text interleaved by publisher. Native extraction was bot-blocked.

## Transcript

001. [0:16](https://www.youtube.com/watch?v=T72nqdC92PM&t=16s)
     All right. Um, hi everyone. Good

002. [0:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=18s)
     afternoon. I'm Krishna. Uh, and I'm a

003. [0:21](https://www.youtube.com/watch?v=T72nqdC92PM&t=21s)
     general manager at Servin. Um today I'm

004. [0:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=24s)
     going to tell you how a three billion

005. [0:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=26s)
     parameter model uh small enough to run

006. [0:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=30s)
     on a single GPU gets state-of-the-art uh

007. [0:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=34s)
     in document AI and beats models 100

008. [0:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=38s)
     times larger in size.

009. [0:41](https://www.youtube.com/watch?v=T72nqdC92PM&t=41s)
     It is also a slightly unusual model in

010. [0:44](https://www.youtube.com/watch?v=T72nqdC92PM&t=44s)
     two ways. Firstly u the language model

011. [0:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=46s)
     used is not a standard transformer. Um

012. [0:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=49s)
     and the entire model building from data

013. [0:52](https://www.youtube.com/watch?v=T72nqdC92PM&t=52s)
     to training to compute uh was done end

014. [0:55](https://www.youtube.com/watch?v=T72nqdC92PM&t=55s)
     to end in India and for English and for

015. [1:00](https://www.youtube.com/watch?v=T72nqdC92PM&t=60s)
     22 official Indian languages uh which I

016. [1:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=63s)
     think uh are personally uh uh one of the

017. [1:05](https://www.youtube.com/watch?v=T72nqdC92PM&t=65s)
     hardest document intelligence problems

018. [1:07](https://www.youtube.com/watch?v=T72nqdC92PM&t=67s)
     uh in the world right now. Um this is

019. [1:10](https://www.youtube.com/watch?v=T72nqdC92PM&t=70s)
     how we went from scratch to SOTA.

020. [1:14](https://www.youtube.com/watch?v=T72nqdC92PM&t=74s)
     Who are we? Uh we are serv uh a

021. [1:16](https://www.youtube.com/watch?v=T72nqdC92PM&t=76s)
     sovereign foundation model company uh in

022. [1:19](https://www.youtube.com/watch?v=T72nqdC92PM&t=79s)
     India. We work across different

023. [1:21](https://www.youtube.com/watch?v=T72nqdC92PM&t=81s)
     modalities voice, text and vision. Uh in

024. [1:25](https://www.youtube.com/watch?v=T72nqdC92PM&t=85s)
     voice we have speech to text and

025. [1:27](https://www.youtube.com/watch?v=T72nqdC92PM&t=87s)
     texttospech models. In text we have uh a

026. [1:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=91s)
     30 billion and 100 billion parameter uh

027. [1:33](https://www.youtube.com/watch?v=T72nqdC92PM&t=93s)
     uh models and in vision we have a

028. [1:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=96s)
     document intelligence model which is

029. [1:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=98s)
     what we are going to talk about today.

030. [1:41](https://www.youtube.com/watch?v=T72nqdC92PM&t=101s)
     Um, India is largely missing from the

031. [1:44](https://www.youtube.com/watch?v=T72nqdC92PM&t=104s)
     machine readable world. Um, according to

032. [1:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=107s)
     a published language distribution study,

033. [1:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=110s)
     well under 1% of the common crawl uh

034. [1:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=114s)
     corpus on which frontier models are

035. [1:56](https://www.youtube.com/watch?v=T72nqdC92PM&t=116s)
     trained uh have uh um Indian language

036. [2:00](https://www.youtube.com/watch?v=T72nqdC92PM&t=120s)
     representation.

037. [2:01](https://www.youtube.com/watch?v=T72nqdC92PM&t=121s)
     Now in several forums you may have heard

038. [2:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=123s)
     Frontier Labs say that um India is their

039. [2:07](https://www.youtube.com/watch?v=T72nqdC92PM&t=127s)
     um India is one of their larger uh uh

040. [2:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=129s)
     and fastly growing markets and to that

041. [2:13](https://www.youtube.com/watch?v=T72nqdC92PM&t=133s)
     end um India is still missing uh in

042. [2:16](https://www.youtube.com/watch?v=T72nqdC92PM&t=136s)
     terms of data from frontier models that

043. [2:19](https://www.youtube.com/watch?v=T72nqdC92PM&t=139s)
     uh um are being trained every day here.

044. [2:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=142s)
     Now why is that? Uh primarily not

045. [2:25](https://www.youtube.com/watch?v=T72nqdC92PM&t=145s)
     because there is uh a lack of data or

046. [2:28](https://www.youtube.com/watch?v=T72nqdC92PM&t=148s)
     the knowledge does not exist. It is

047. [2:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=150s)
     because the data has never been

048. [2:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=151s)
     digitized and we are solving that

049. [2:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=154s)
     problem at server.

050. [2:37](https://www.youtube.com/watch?v=T72nqdC92PM&t=157s)
     Um why is Indic document intelligence

051. [2:40](https://www.youtube.com/watch?v=T72nqdC92PM&t=160s)
     hard? Uh firstly the goal is that of

052. [2:44](https://www.youtube.com/watch?v=T72nqdC92PM&t=164s)
     knowledge extraction not just purely

053. [2:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=166s)
     text extraction. Uh extracting pure text

054. [2:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=169s)
     without logical coherence is

055. [2:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=171s)
     meaningless. And secondly in index

056. [2:55](https://www.youtube.com/watch?v=T72nqdC92PM&t=175s)
     scripts the shape of uh the words and

057. [2:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=178s)
     the language you see are very different

058. [3:01](https://www.youtube.com/watch?v=T72nqdC92PM&t=181s)
     from what a machine sees. that is Indian

059. [3:04](https://www.youtube.com/watch?v=T72nqdC92PM&t=184s)
     languages have a complex uh set of uni

060. [3:07](https://www.youtube.com/watch?v=T72nqdC92PM&t=187s)
     codes fused together to get right the

061. [3:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=189s)
     language model needs to be strong at all

062. [3:12](https://www.youtube.com/watch?v=T72nqdC92PM&t=192s)
     22 languages. Third, majority of Indian

063. [3:16](https://www.youtube.com/watch?v=T72nqdC92PM&t=196s)
     languages can be considered low resource

064. [3:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=198s)
     due to which there is a lot of uh um

065. [3:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=202s)
     lack in data today to train these

066. [3:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=204s)
     models.

067. [3:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=206s)
     Our answer to this is server vision

068. [3:28](https://www.youtube.com/watch?v=T72nqdC92PM&t=208s)
     India's first sovereign vision language

069. [3:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=210s)
     model built from scratch. um a three

070. [3:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=214s)
     billion parameter model with state space

071. [3:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=216s)
     architecture

072. [3:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=218s)
     data compute and training all of which

073. [3:40](https://www.youtube.com/watch?v=T72nqdC92PM&t=220s)
     done in India. When we started the

074. [3:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=223s)
     initial work in late 2025 most VLMs uh

075. [3:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=227s)
     in the OCR space were monolith VLMs. uh

076. [3:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=231s)
     they performed page level OCR and we at

077. [3:55](https://www.youtube.com/watch?v=T72nqdC92PM&t=235s)
     the time took a contrarian bet to focus

078. [3:57](https://www.youtube.com/watch?v=T72nqdC92PM&t=237s)
     on block level OCR instead adding a

079. [4:00](https://www.youtube.com/watch?v=T72nqdC92PM&t=240s)
     document hardness around the model. Um a

080. [4:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=243s)
     lot of models since then uh released uh

081. [4:06](https://www.youtube.com/watch?v=T72nqdC92PM&t=246s)
     uh recently in 2026 have converged onto

082. [4:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=249s)
     the same uh hardness plus small model

083. [4:12](https://www.youtube.com/watch?v=T72nqdC92PM&t=252s)
     paradigm for OCR which shows a lot of

084. [4:14](https://www.youtube.com/watch?v=T72nqdC92PM&t=254s)
     value in the direction we uh set off.

085. [4:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=258s)
     Serverom vision in particular uh has two

086. [4:20](https://www.youtube.com/watch?v=T72nqdC92PM&t=260s)
     hardness modules one for layout and one

087. [4:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=262s)
     for reading hardness and a state space

088. [4:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=266s)
     model uh VLM for block level OCR.

089. [4:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=271s)
     Again um today uh why do we use state

090. [4:35](https://www.youtube.com/watch?v=T72nqdC92PM&t=275s)
     space and not a transformer? Um most OCR

091. [4:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=278s)
     models today uh like general VLMs, open

092. [4:41](https://www.youtube.com/watch?v=T72nqdC92PM&t=281s)
     source VLMs like Quen, Gemma etc. are

093. [4:44](https://www.youtube.com/watch?v=T72nqdC92PM&t=284s)
     all transformers based. We took an

094. [4:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=286s)
     alternate approach uh using an SSM. Why?

095. [4:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=291s)
     Both are fundamentally sequenced models

096. [4:53](https://www.youtube.com/watch?v=T72nqdC92PM&t=293s)
     transformers and SSMs but with very

097. [4:56](https://www.youtube.com/watch?v=T72nqdC92PM&t=296s)
     different underlying mechanics. A

098. [4:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=298s)
     transformer has every token look at

099. [5:01](https://www.youtube.com/watch?v=T72nqdC92PM&t=301s)
     every other token where the compute

100. [5:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=303s)
     grows with square of the sequence

101. [5:06](https://www.youtube.com/watch?v=T72nqdC92PM&t=306s)
     length. Uh that is the L cross L

102. [5:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=309s)
     interactions and the memory goes as the

103. [5:12](https://www.youtube.com/watch?v=T72nqdC92PM&t=312s)
     sequence grows as well. Now on the other

104. [5:15](https://www.youtube.com/watch?v=T72nqdC92PM&t=315s)
     hand, SSMs have a single state. They

105. [5:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=318s)
     maintain a single state through the

106. [5:20](https://www.youtube.com/watch?v=T72nqdC92PM&t=320s)
     sequence updating it token by token. Now

107. [5:23](https://www.youtube.com/watch?v=T72nqdC92PM&t=323s)
     as compute grows only linearly, the

108. [5:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=326s)
     memory stays constant for SSMS. Now why

109. [5:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=330s)
     is this the right uh architecture for

110. [5:32](https://www.youtube.com/watch?v=T72nqdC92PM&t=332s)
     OCR? It really depends on the uh uh

111. [5:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=336s)
     trade-offs here uh for long documents in

112. [5:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=338s)
     particular which can lead up to uh uh 5

113. [5:41](https://www.youtube.com/watch?v=T72nqdC92PM&t=341s)
     to 10,000 uh visual tokens per page and

114. [5:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=346s)
     quadratic complexity of you know uh

115. [5:48](https://www.youtube.com/watch?v=T72nqdC92PM&t=348s)
     compute and memory becomes very

116. [5:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=350s)
     expensive for inference. On the other

117. [5:52](https://www.youtube.com/watch?v=T72nqdC92PM&t=352s)
     hand,

118. [5:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=354s)
     um doing block level OCR with somewhat

119. [5:57](https://www.youtube.com/watch?v=T72nqdC92PM&t=357s)
     of a lossy recall using SSMs can be

120. [6:00](https://www.youtube.com/watch?v=T72nqdC92PM&t=360s)
     justifi justified to uh um avoid high

121. [6:04](https://www.youtube.com/watch?v=T72nqdC92PM&t=364s)
     compute costs imposed by transformers.

122. [6:08](https://www.youtube.com/watch?v=T72nqdC92PM&t=368s)
     So how do you actually train this? We

123. [6:12](https://www.youtube.com/watch?v=T72nqdC92PM&t=372s)
     built a staged curriculum four stages

124. [6:14](https://www.youtube.com/watch?v=T72nqdC92PM&t=374s)
     each uh building on the last um stage

125. [6:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=378s)
     one is texton pre-training uh 13

126. [6:21](https://www.youtube.com/watch?v=T72nqdC92PM&t=381s)
     trillion tokens across English, Indian

127. [6:23](https://www.youtube.com/watch?v=T72nqdC92PM&t=383s)
     language, text, math and code. This

128. [6:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=386s)
     builds the three billion parameters

129. [6:28](https://www.youtube.com/watch?v=T72nqdC92PM&t=388s)
     language backbone and a strong language

130. [6:32](https://www.youtube.com/watch?v=T72nqdC92PM&t=392s)
     prior is what lets the model resolve a

131. [6:35](https://www.youtube.com/watch?v=T72nqdC92PM&t=395s)
     smudged or an ambiguous text from the

132. [6:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=398s)
     image. the same way you can read a half

133. [6:41](https://www.youtube.com/watch?v=T72nqdC92PM&t=401s)
     blurred word because you know which word

134. [6:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=403s)
     is supposed to uh u be at the right

135. [6:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=406s)
     place. So we focused on building the

136. [6:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=409s)
     competence of the language model first

137. [6:52](https://www.youtube.com/watch?v=T72nqdC92PM&t=412s)
     uh before the model ever even sees a

138. [6:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=414s)
     pixel. Stage two is where we performed

139. [6:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=418s)
     continual pre-training uh on 300 million

140. [7:01](https://www.youtube.com/watch?v=T72nqdC92PM&t=421s)
     image text pairs. This teaches the

141. [7:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=423s)
     language model general vision

142. [7:05](https://www.youtube.com/watch?v=T72nqdC92PM&t=425s)
     capabilities and teaches how to see how

143. [7:07](https://www.youtube.com/watch?v=T72nqdC92PM&t=427s)
     to interpret pixels and so on. Then

144. [7:10](https://www.youtube.com/watch?v=T72nqdC92PM&t=430s)
     comes stage three where we performed uh

145. [7:12](https://www.youtube.com/watch?v=T72nqdC92PM&t=432s)
     supervised fine-tuning on 100 uh uh

146. [7:15](https://www.youtube.com/watch?v=T72nqdC92PM&t=435s)
     million uh OCR uh samples. Now the um

147. [7:21](https://www.youtube.com/watch?v=T72nqdC92PM&t=441s)
     stage three is primarily focused on

148. [7:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=444s)
     letting a general VM model become strong

149. [7:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=446s)
     at OCR. What that includes is having

150. [7:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=450s)
     diverse data across all 22 languages and

151. [7:33](https://www.youtube.com/watch?v=T72nqdC92PM&t=453s)
     English and also incorporating all kinds

152. [7:35](https://www.youtube.com/watch?v=T72nqdC92PM&t=455s)
     of uh uh document components such as

153. [7:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=459s)
     tables and uh um equations and

154. [7:42](https://www.youtube.com/watch?v=T72nqdC92PM&t=462s)
     handwritten documents and so forth. Now

155. [7:45](https://www.youtube.com/watch?v=T72nqdC92PM&t=465s)
     and stage four is re reinforcement

156. [7:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=467s)
     learning which helps push past the

157. [7:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=470s)
     ceiling of whatever uh supervised

158. [7:53](https://www.youtube.com/watch?v=T72nqdC92PM&t=473s)
     fine-tuning is able to achieve. Here you

159. [7:55](https://www.youtube.com/watch?v=T72nqdC92PM&t=475s)
     will see this is a standard recipe.

160. [7:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=478s)
     However, the moat here is the two things

161. [8:02](https://www.youtube.com/watch?v=T72nqdC92PM&t=482s)
     underneath the data layer and the eval

162. [8:05](https://www.youtube.com/watch?v=T72nqdC92PM&t=485s)
     layer. Um the first is the data engine.

163. [8:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=489s)
     For most of the 22 languages, there is

164. [8:11](https://www.youtube.com/watch?v=T72nqdC92PM&t=491s)
     no label data available readily.

165. [8:13](https://www.youtube.com/watch?v=T72nqdC92PM&t=493s)
     When label data does not exist, building

166. [8:17](https://www.youtube.com/watch?v=T72nqdC92PM&t=497s)
     the data engine becomes hard. And that

167. [8:20](https://www.youtube.com/watch?v=T72nqdC92PM&t=500s)
     is something we have done extensively.

168. [8:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=502s)
     We've built pipelines to create

169. [8:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=504s)
     synthetic data and doc data from real

170. [8:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=506s)
     documents and also helped

171. [8:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=510s)
     build the uh pipeline for continuously

172. [8:33](https://www.youtube.com/watch?v=T72nqdC92PM&t=513s)
     improving the data that goes into

173. [8:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=516s)
     training based on the eval performance

174. [8:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=518s)
     and so on. So we are currently actively

175. [8:40](https://www.youtube.com/watch?v=T72nqdC92PM&t=520s)
     looking at the paradigm of RLMs um as uh

176. [8:44](https://www.youtube.com/watch?v=T72nqdC92PM&t=524s)
     uh we explore the agentic vision

177. [8:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=526s)
     capabilities for our models in the

178. [8:48](https://www.youtube.com/watch?v=T72nqdC92PM&t=528s)
     upcoming releases. The second mode is

179. [8:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=531s)
     the eval. You cannot reach

180. [8:53](https://www.youtube.com/watch?v=T72nqdC92PM&t=533s)
     state-of-the-art if uh um you cannot

181. [8:56](https://www.youtube.com/watch?v=T72nqdC92PM&t=536s)
     measure how well your model performs. We

182. [8:59](https://www.youtube.com/watch?v=T72nqdC92PM&t=539s)
     have curated extensive evals to ensure

183. [9:02](https://www.youtube.com/watch?v=T72nqdC92PM&t=542s)
     what we are measuring is truly sota and

184. [9:04](https://www.youtube.com/watch?v=T72nqdC92PM&t=544s)
     also truly meaningful in terms of

185. [9:06](https://www.youtube.com/watch?v=T72nqdC92PM&t=546s)
     usefulness for end uh uh users. So I

186. [9:11](https://www.youtube.com/watch?v=T72nqdC92PM&t=551s)
     want to take just a minute to dwell on

187. [9:13](https://www.youtube.com/watch?v=T72nqdC92PM&t=553s)
     our RL pipeline uh stage four because uh

188. [9:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=558s)
     a lot of gain comes from RL. Essentially

189. [9:21](https://www.youtube.com/watch?v=T72nqdC92PM&t=561s)
     in OCR correctness is a machine readable

190. [9:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=564s)
     problem right a lot of tests can be set

191. [9:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=566s)
     up to uh um reward and score the models

192. [9:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=571s)
     against uh uh these uh samples that you

193. [9:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=574s)
     create. And in the world of

194. [9:37](https://www.youtube.com/watch?v=T72nqdC92PM&t=577s)
     deterministic OCR, these are all machine

195. [9:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=579s)
     uh uh verifiable. Hence, RL gives us a

196. [9:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=583s)
     major boost.

197. [9:45](https://www.youtube.com/watch?v=T72nqdC92PM&t=585s)
     Sample a group, score with unit tests,

198. [9:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=587s)
     reinforce what the average uh uh value

199. [9:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=591s)
     to beat is, and then repeat the process.

200. [9:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=594s)
     And this makes RLVR for OCR very very

201. [9:56](https://www.youtube.com/watch?v=T72nqdC92PM&t=596s)
     scalable.

202. [9:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=598s)
     Now after all the from scratch training

203. [10:01](https://www.youtube.com/watch?v=T72nqdC92PM&t=601s)
     we've done and the data effort we've

204. [10:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=603s)
     made we were able to establish sot in

205. [10:06](https://www.youtube.com/watch?v=T72nqdC92PM&t=606s)
     two of uh the global English benchmarks

206. [10:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=609s)
     one is CRB bench and the other is

207. [10:12](https://www.youtube.com/watch?v=T72nqdC92PM&t=612s)
     omnidoc bench at launch we were at 84.3

208. [10:16](https://www.youtube.com/watch?v=T72nqdC92PM&t=616s)
     on CR and then 93.2 into on omnidok

209. [10:19](https://www.youtube.com/watch?v=T72nqdC92PM&t=619s)
     bench. Um the models uh that have

210. [10:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=622s)
     released since have moved the needle

211. [10:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=624s)
     quite a bit and we'll soon have a a

212. [10:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=626s)
     stronger model in the global leaderboard

213. [10:29](https://www.youtube.com/watch?v=T72nqdC92PM&t=629s)
     as well.

214. [10:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=631s)
     Secondly and more importantly um on 22

215. [10:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=634s)
     Indian languages we have an unbeaten

216. [10:37](https://www.youtube.com/watch?v=T72nqdC92PM&t=637s)
     lead even compared to all the frontier

217. [10:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=639s)
     models such as Gemini and uh chat GPT

218. [10:42](https://www.youtube.com/watch?v=T72nqdC92PM&t=642s)
     and Opus and so on. And this is where

219. [10:45](https://www.youtube.com/watch?v=T72nqdC92PM&t=645s)
     we've extended the lead significantly

220. [10:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=647s)
     and we remain uh uh strong compared to

221. [10:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=650s)
     all of these newer models that have come

222. [10:52](https://www.youtube.com/watch?v=T72nqdC92PM&t=652s)
     in.

223. [10:53](https://www.youtube.com/watch?v=T72nqdC92PM&t=653s)
     Now server vision pars our agentic

224. [10:57](https://www.youtube.com/watch?v=T72nqdC92PM&t=657s)
     document intelligence workbench called

225. [10:59](https://www.youtube.com/watch?v=T72nqdC92PM&t=659s)
     aure where we enable

226. [11:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=663s)
     human in the loop agentic digitizations

227. [11:06](https://www.youtube.com/watch?v=T72nqdC92PM&t=666s)
     uh and uh extractions and then

228. [11:08](https://www.youtube.com/watch?v=T72nqdC92PM&t=668s)
     injections for various uh downstream uh

229. [11:11](https://www.youtube.com/watch?v=T72nqdC92PM&t=671s)
     document intelligence problems. We

230. [11:13](https://www.youtube.com/watch?v=T72nqdC92PM&t=673s)
     provide confidence scores um and we uh

231. [11:16](https://www.youtube.com/watch?v=T72nqdC92PM&t=676s)
     have block level grounding and then also

232. [11:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=678s)
     the ability to do uh agentic proof

233. [11:20](https://www.youtube.com/watch?v=T72nqdC92PM&t=680s)
     reading etc.

234. [11:23](https://www.youtube.com/watch?v=T72nqdC92PM&t=683s)
     Now benchmarks and soda are uh uh one

235. [11:27](https://www.youtube.com/watch?v=T72nqdC92PM&t=687s)
     thing they have their place. Today some

236. [11:29](https://www.youtube.com/watch?v=T72nqdC92PM&t=689s)
     of the largest enterprises in the world

237. [11:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=691s)
     from insurance to banking to governments

238. [11:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=694s)
     to historical preservation organizations

239. [11:37](https://www.youtube.com/watch?v=T72nqdC92PM&t=697s)
     are using server vision to digitize more

240. [11:40](https://www.youtube.com/watch?v=T72nqdC92PM&t=700s)
     than 35 million pages across English and

241. [11:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=703s)
     uh uh 22 Indian languages. The model is

242. [11:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=707s)
     available as API and on prem and then

243. [11:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=711s)
     the agentic platform.

244. [11:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=714s)
     So in conclusion until 4 months ago uh

245. [11:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=718s)
     there was no sovereign model uh from

246. [12:00](https://www.youtube.com/watch?v=T72nqdC92PM&t=720s)
     India. Today we have server vision which

247. [12:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=723s)
     was trained from scratch and has

248. [12:05](https://www.youtube.com/watch?v=T72nqdC92PM&t=725s)
     established sot um at a price point that

249. [12:08](https://www.youtube.com/watch?v=T72nqdC92PM&t=728s)
     is extremely competitive with uh all the

250. [12:11](https://www.youtube.com/watch?v=T72nqdC92PM&t=731s)
     other solutions including open and close

251. [12:14](https://www.youtube.com/watch?v=T72nqdC92PM&t=734s)
     source. Uh first we've started by uh uh

252. [12:17](https://www.youtube.com/watch?v=T72nqdC92PM&t=737s)
     solving some of the hardest problems for

253. [12:19](https://www.youtube.com/watch?v=T72nqdC92PM&t=739s)
     Indian language document intelligence.

254. [12:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=742s)
     Soon uh we'll be releasing general

255. [12:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=744s)
     purpose uh VLMs which are capable of

256. [12:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=746s)
     much more uh uh vision capabilities and

257. [12:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=750s)
     uh look forward to uh uh all of you

258. [12:32](https://www.youtube.com/watch?v=T72nqdC92PM&t=752s)
     trying out our models. Thank you.

259. [12:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=756s)
     \[applause\]

260. [12:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=759s)
     Happy to answer any questions. Yeah.

261. [12:48](https://www.youtube.com/watch?v=T72nqdC92PM&t=768s)
     Yes.

262. [12:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=769s)
     >\> Yes. Absolutely. Uh in general, the

263. [12:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=771s)
     language capability of the 22 languages

264. [12:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=774s)
     enhances English uh by quite a margin.

265. [12:57](https://www.youtube.com/watch?v=T72nqdC92PM&t=777s)
     And this is applicable to any low

266. [12:59](https://www.youtube.com/watch?v=T72nqdC92PM&t=779s)
     resource language, not just Indian low

267. [13:02](https://www.youtube.com/watch?v=T72nqdC92PM&t=782s)
     resource languages.

268. [13:05](https://www.youtube.com/watch?v=T72nqdC92PM&t=785s)
     >\> Yeah.

269. [13:27](https://www.youtube.com/watch?v=T72nqdC92PM&t=807s)
     Right. Um we don't quite go in that

270. [13:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=810s)
     direction with this model because this

271. [13:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=811s)
     is a vision focused uh uh model wherein

272. [13:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=814s)
     we are focused on extracting information

273. [13:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=816s)
     or knowledge from documents. But yes,

274. [13:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=819s)
     there could be uh some parallels to um

275. [13:42](https://www.youtube.com/watch?v=T72nqdC92PM&t=822s)
     helping models use general languages to

276. [13:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=826s)
     speed up coding as well. But yeah,

277. [13:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=827s)
     that's not the uh periphery of this uh

278. [13:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=830s)
     uh work.

279. [13:53](https://www.youtube.com/watch?v=T72nqdC92PM&t=833s)
     Yeah.

280. [14:10](https://www.youtube.com/watch?v=T72nqdC92PM&t=850s)
     Right. Um so there are two things uh we

281. [14:13](https://www.youtube.com/watch?v=T72nqdC92PM&t=853s)
     uh create artificial documents synthetic

282. [14:15](https://www.youtube.com/watch?v=T72nqdC92PM&t=855s)
     documents as they are called for general

283. [14:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=858s)
     post-raining uh that includes SFT and

284. [14:21](https://www.youtube.com/watch?v=T72nqdC92PM&t=861s)
     RL. Um however coming to your specific

285. [14:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=864s)
     question on RL uh we don't uh you can

286. [14:27](https://www.youtube.com/watch?v=T72nqdC92PM&t=867s)
     generate uh synthetic documents there as

287. [14:29](https://www.youtube.com/watch?v=T72nqdC92PM&t=869s)
     well. However, um the best thing to do

288. [14:32](https://www.youtube.com/watch?v=T72nqdC92PM&t=872s)
     is to take real world documents complex

289. [14:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=874s)
     enough that uh help you set up unit

290. [14:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=876s)
     tests or different kinds of uh uh

291. [14:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=879s)
     rewards, right? like say a a reward

292. [14:42](https://www.youtube.com/watch?v=T72nqdC92PM&t=882s)
     based on character error rate or a a

293. [14:45](https://www.youtube.com/watch?v=T72nqdC92PM&t=885s)
     reward based on table structure or a

294. [14:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=887s)
     math equation or something uh that is

295. [14:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=889s)
     pertinent to a language or like grammar

296. [14:52](https://www.youtube.com/watch?v=T72nqdC92PM&t=892s)
     rewards or so on and then help the model

297. [14:55](https://www.youtube.com/watch?v=T72nqdC92PM&t=895s)
     iteratively improve based on uh um rules

298. [14:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=898s)
     that the model is able to produce at

299. [14:59](https://www.youtube.com/watch?v=T72nqdC92PM&t=899s)
     different uh u settings. Yeah. Yes.

300. [15:21](https://www.youtube.com/watch?v=T72nqdC92PM&t=921s)
     Sorry, did you say big fan of Chundra?

301. [15:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=924s)
     >\> All right. Uh, that's from a different

302. [15:25](https://www.youtube.com/watch?v=T72nqdC92PM&t=925s)
     lab. Uh, I'm also a big fan of the lab

303. [15:28](https://www.youtube.com/watch?v=T72nqdC92PM&t=928s)
     that produced Chundra. But yes, took

304. [15:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=930s)
     your question uh on Indic benchmark.

305. [15:32](https://www.youtube.com/watch?v=T72nqdC92PM&t=932s)
     Yes, we will release the server indic

306. [15:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=934s)
     benchmark that we have created for 22

307. [15:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=938s)
     languages and it uh spans um a a huge

308. [15:42](https://www.youtube.com/watch?v=T72nqdC92PM&t=942s)
     time period starting from 1800s until

309. [15:45](https://www.youtube.com/watch?v=T72nqdC92PM&t=945s)
     modern day and also different kinds of

310. [15:46](https://www.youtube.com/watch?v=T72nqdC92PM&t=946s)
     layouts, different kinds of documents in

311. [15:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=949s)
     Indian languages. You can imagine

312. [15:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=950s)
     documents with pros, poetry, literature,

313. [15:53](https://www.youtube.com/watch?v=T72nqdC92PM&t=953s)
     uh tables, finance and all of those

314. [15:55](https://www.youtube.com/watch?v=T72nqdC92PM&t=955s)
     things. We'll soon release that

315. [15:57](https://www.youtube.com/watch?v=T72nqdC92PM&t=957s)
     benchmark uh in public as well.

316. [16:25](https://www.youtube.com/watch?v=T72nqdC92PM&t=985s)
     So translation is again uh

317. [16:27](https://www.youtube.com/watch?v=T72nqdC92PM&t=987s)
     transliteration is again not directly

318. [16:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=990s)
     involved here because in OCR what we

319. [16:32](https://www.youtube.com/watch?v=T72nqdC92PM&t=992s)
     care about is high fidelity extraction

320. [16:35](https://www.youtube.com/watch?v=T72nqdC92PM&t=995s)
     right uh you want even if there is a

321. [16:37](https://www.youtube.com/watch?v=T72nqdC92PM&t=997s)
     mistake in an image you want that

322. [16:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=998s)
     mistake to be extracted correctly and

323. [16:40](https://www.youtube.com/watch?v=T72nqdC92PM&t=1000s)
     not the model uh uh making changes at

324. [16:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=1003s)
     whim uh hence that is not directly

325. [16:45](https://www.youtube.com/watch?v=T72nqdC92PM&t=1005s)
     applicable but yes uh what we see is a

326. [16:48](https://www.youtube.com/watch?v=T72nqdC92PM&t=1008s)
     lot of data that is coming through

327. [16:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=1010s)
     transliteration for even OCR training

328. [16:52](https://www.youtube.com/watch?v=T72nqdC92PM&t=1012s)
     now and the um jury is out on what is

329. [16:56](https://www.youtube.com/watch?v=T72nqdC92PM&t=1016s)
     the quality of that data and how useful

330. [16:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=1018s)
     it is etc

331. [17:00](https://www.youtube.com/watch?v=T72nqdC92PM&t=1020s)
     Yeah.

332. [17:27](https://www.youtube.com/watch?v=T72nqdC92PM&t=1047s)
     Right. Um there are few things to

333. [17:29](https://www.youtube.com/watch?v=T72nqdC92PM&t=1049s)
     consider. Um first is no other model

334. [17:33](https://www.youtube.com/watch?v=T72nqdC92PM&t=1053s)
     frontier uh closed source or open model

335. [17:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=1056s)
     does well with complex Indian language

336. [17:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=1059s)
     documents right so for a size of uh for

337. [17:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=1063s)
     a country with 1.4 4 billion people you

338. [17:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=1067s)
     want to be able to address their

339. [17:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=1069s)
     day-to-day lives in uh uh terms of

340. [17:51](https://www.youtube.com/watch?v=T72nqdC92PM&t=1071s)
     document intelligence problems because

341. [17:53](https://www.youtube.com/watch?v=T72nqdC92PM&t=1073s)
     there is a lot of paperwork in India

342. [17:55](https://www.youtube.com/watch?v=T72nqdC92PM&t=1075s)
     right it is a up and cominging country

343. [17:58](https://www.youtube.com/watch?v=T72nqdC92PM&t=1078s)
     and it's still being digitized as we

344. [18:00](https://www.youtube.com/watch?v=T72nqdC92PM&t=1080s)
     speak and it's important that

345. [18:02](https://www.youtube.com/watch?v=T72nqdC92PM&t=1082s)
     representation or ability to digitize

346. [18:04](https://www.youtube.com/watch?v=T72nqdC92PM&t=1084s)
     the country exists to begin with.

347. [18:06](https://www.youtube.com/watch?v=T72nqdC92PM&t=1086s)
     Secondly on uh the training side what we

348. [18:10](https://www.youtube.com/watch?v=T72nqdC92PM&t=1090s)
     have uh uh done in particular is to

349. [18:14](https://www.youtube.com/watch?v=T72nqdC92PM&t=1094s)
     create data that can be added to a lot

350. [18:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=1098s)
     of training downstream. So uh we are at

351. [18:20](https://www.youtube.com/watch?v=T72nqdC92PM&t=1100s)
     a very early stage in terms of AI

352. [18:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=1102s)
     becoming you know a regular parts of our

353. [18:26](https://www.youtube.com/watch?v=T72nqdC92PM&t=1106s)
     lives and we need the data to start to

354. [18:29](https://www.youtube.com/watch?v=T72nqdC92PM&t=1109s)
     be able to eventually get to a place

355. [18:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=1110s)
     where we can uh have personalized agents

356. [18:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=1114s)
     in the language you prefer in language I

357. [18:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=1116s)
     prefer and however I want in uh uh in

358. [18:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=1119s)
     some so to do all of that we need to

359. [18:41](https://www.youtube.com/watch?v=T72nqdC92PM&t=1121s)
     start somewhere and the data needs to be

360. [18:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=1123s)
     created and if the data is of good

361. [18:45](https://www.youtube.com/watch?v=T72nqdC92PM&t=1125s)
     quality then that helps the model become

362. [18:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=1127s)
     sota and If a model is sot then uh from

363. [18:52](https://www.youtube.com/watch?v=T72nqdC92PM&t=1132s)
     uh insurance agencies to government

364. [18:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=1134s)
     organizations to others who care about

365. [18:57](https://www.youtube.com/watch?v=T72nqdC92PM&t=1137s)
     sovereignity in AI right uh as a

366. [18:59](https://www.youtube.com/watch?v=T72nqdC92PM&t=1139s)
     government body I cannot have a model

367. [19:02](https://www.youtube.com/watch?v=T72nqdC92PM&t=1142s)
     deployed elsewhere and I don't know

368. [19:03](https://www.youtube.com/watch?v=T72nqdC92PM&t=1143s)
     where the data is going for uh uh the

369. [19:06](https://www.youtube.com/watch?v=T72nqdC92PM&t=1146s)
     transcriptions so I need to be able to

370. [19:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=1149s)
     control where the data is sent and when

371. [19:11](https://www.youtube.com/watch?v=T72nqdC92PM&t=1151s)
     it is used how much it is used etc. So

372. [19:14](https://www.youtube.com/watch?v=T72nqdC92PM&t=1154s)
     sovereignity becomes very crucial and

373. [19:16](https://www.youtube.com/watch?v=T72nqdC92PM&t=1156s)
     hence this model really is now uh uh

374. [19:18](https://www.youtube.com/watch?v=T72nqdC92PM&t=1158s)
     like it's been what four months since we

375. [19:20](https://www.youtube.com/watch?v=T72nqdC92PM&t=1160s)
     launched and already we are we are

376. [19:22](https://www.youtube.com/watch?v=T72nqdC92PM&t=1162s)
     digitizing 35 million pages. So that is

377. [19:25](https://www.youtube.com/watch?v=T72nqdC92PM&t=1165s)
     that shows that the market was waiting

378. [19:27](https://www.youtube.com/watch?v=T72nqdC92PM&t=1167s)
     for something sovereign in this space

379. [19:28](https://www.youtube.com/watch?v=T72nqdC92PM&t=1168s)
     that can really kickstart uh the AI

380. [19:31](https://www.youtube.com/watch?v=T72nqdC92PM&t=1171s)
     digitization wave in India. So yeah

381. [19:34](https://www.youtube.com/watch?v=T72nqdC92PM&t=1174s)
     primarily like three aspects one on uh

382. [19:36](https://www.youtube.com/watch?v=T72nqdC92PM&t=1176s)
     sovereignity the other is the model uh

383. [19:39](https://www.youtube.com/watch?v=T72nqdC92PM&t=1179s)
     capability itself and the third is data

384. [19:41](https://www.youtube.com/watch?v=T72nqdC92PM&t=1181s)
     uh that is required to train these

385. [19:43](https://www.youtube.com/watch?v=T72nqdC92PM&t=1183s)
     models.

386. [19:54](https://www.youtube.com/watch?v=T72nqdC92PM&t=1194s)
     Yeah, it is it is uh um 40% uh indic and

387. [19:59](https://www.youtube.com/watch?v=T72nqdC92PM&t=1199s)
     then uh the rest is English and

388. [20:01](https://www.youtube.com/watch?v=T72nqdC92PM&t=1201s)
     comprises of math and code etc.

389. [20:08](https://www.youtube.com/watch?v=T72nqdC92PM&t=1208s)
     >\> All right.

390. [20:09](https://www.youtube.com/watch?v=T72nqdC92PM&t=1209s)
     Just a curious question.

391. [20:24](https://www.youtube.com/watch?v=T72nqdC92PM&t=1224s)
     Um currently the uh the deployments

392. [20:28](https://www.youtube.com/watch?v=T72nqdC92PM&t=1228s)
     we've made uh with this model are in

393. [20:30](https://www.youtube.com/watch?v=T72nqdC92PM&t=1230s)
     different states uh uh trying to

394. [20:33](https://www.youtube.com/watch?v=T72nqdC92PM&t=1233s)
     digitize regional languages and along

395. [20:35](https://www.youtube.com/watch?v=T72nqdC92PM&t=1235s)
     with all the English and mixed language

396. [20:38](https://www.youtube.com/watch?v=T72nqdC92PM&t=1238s)
     uh uh documents and hence we'll soon uh

397. [20:42](https://www.youtube.com/watch?v=T72nqdC92PM&t=1242s)
     be able to train with the um uh feedback

398. [20:47](https://www.youtube.com/watch?v=T72nqdC92PM&t=1247s)
     we get from uh the current deployment.

399. [20:49](https://www.youtube.com/watch?v=T72nqdC92PM&t=1249s)
     So yeah, we have started that uh

400. [20:50](https://www.youtube.com/watch?v=T72nqdC92PM&t=1250s)
     pipeline as well.

401. ![AI Engineer World's Fair title in white on a black background.](https://assets.ai.engineer/sites/aiecode2025/sha256/f1262899667d21f8fab0b090c1d1be7279204b46b4b2470d8b921a8b5e1cef7d.webp)


     AI Engineer World's Fair



     AI Engineer World's Fair title in white on a black background.

     Text in image

     ```
     AI Engineer
     World’s Fair

     HTTPS://AI.ENGINEER
     ```





     [21:01](https://www.youtube.com/watch?v=T72nqdC92PM&t=1261s)

402. [21:07](https://www.youtube.com/watch?v=T72nqdC92PM&t=1267s)
     >\> \[music\]


