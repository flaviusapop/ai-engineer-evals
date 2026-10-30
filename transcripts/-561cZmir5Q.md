# From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs

Source: https://www.youtube.com/watch?v=-561cZmir5Q

Upload date (publisher UTC): 2026-07-19

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/bf/bf118a4cb2e74980ce3a676ef38071e17cf7eb99bd5cbdb4b72ffe378f607f4d.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[12.20s] Okay, let's get started. Uh, my name is Akram. I'm a machine learning engineer at Altos Labs. Altos Labs is a biotech startup, and the goal is to restore cell health and resilience through cellular rejuvenation to reverse disease and disabilities that can happen throughout the life.

[32.44s] And the title of my talk is, uh, From Tokens to Cells, and this is, uh, my kind of view as someone, mm, without bio background to kind of looking into the engineering challenges of foundation models for single-cell biology.

[51.18s] And what I want to talk about, first, what is single cell? Why do we care about single cell? How do, how do we measure it? What are the problems with the data, getting the data?

[61.48s] And then looking at current state-of-the-art foundation models, and then some takeaways in the end.

[69.06s] Uh, so what is single cell, and why do we care about it? I would like to start with my favorite example, Yamanaka factor. In two thousand and six, Shinya Yamanaka discovered four transcription factors that are for a specific type of, uh, proteins that when they were overexpressed in a cell, uh, they did it for, uh, in a

[91.92s] cell, uh, which was a age-old skin cell. It could reprogram the skin cell or the skin cell to embryonic stem cell-like state. So basically from cell type skin cell old, it could reprogram it back to a young embryonic stem cell type,

[113.22s] uh, type. And this was a breakthrough for biology, and then got him Nobel Prize later in two thousand twelve, uh, because of the application and the new chapters, possibilities for medicine, from regenerative medicine for, like, to be able to kind of regenerate tissues or organs, uh, when we can, like, reprogram a specific cell to any cell that

[138.26s] we want to partial reprogramming and aging application. For partial reprogramming specifically is that we can also turn out that we can also only change the age of the cell.

[149.60s] We don't have to change the type. So by changing the age of the cell, the goal is, the hope is we can restore some of youthful function that we lose throughout life as we age, and then kind of like having this as a medicine, maybe like an mRNA medicine, you know, for curing a disease that we, we,

[169.55s] we encounter as we age. And that's, uh, one example. And then I think this year, two thousand twenty-six, we got the first type of reprogramming medicine. I think it's OSK, and, uh, it's going to be tested in a human.

[187.04s] So it took kind of like twenty, twenty years.

[191.38s] And, uh, and the reason, the other reason is that why we want to study, uh, a single cell is that we would like to model, to have this unified holistic view of single cell, to be able to model cell, and from there, hopefully, we can model tissue and organ and then the entire human.

[211.86s] And there are, like, projects like Human Cell Atlas that actually started this effort, this initiative, and then they, like, you know, they have, they have mapped every single cell inside human.

[224.01s] And the goal ultimately is something like we maybe for, uh, ultimately some, after some long time we can actually, like, actually model, uh, like, mo-model human body or there are terminologies like virtual cell, virtual tissue, virtual human, digital twins.

[242.28s] They're all saying the same thing that the more we can model this, uh, living organisms,

[250.44s] the better we are in understanding our body and then how

[254.90s] we can treat a medicine, we can develop drugs.

[259.82s] And, uh, the, the other, uh, uh, um, the other problem is that, so we, you know, I think for this audience, we know about Moore's Law. The compute is getting, like, double every year.

[272.40s] And then we have exact opposite on drug development. Basically, the number of drugs that develop each year is kind of declining, which is surprising with all the advances in technology, in AI.

[285.60s] And this is surprising to see. And then drug development is a field that failure is, you know, very normal. Maybe the acceptance ra-rate is kind of like, you know, five percent or even less.

[297.60s] And, uh, when we're looking at drug development pipeline from the early, like, research and development all the way to preclinical, clinical trial and then the final, uh, stage, the whole, uh, pipeline, it could take up to ten years easily, and then it costs, it can cost billions.

[316.52s] And the goal here is that with the advances of AI and also, like, with this, uh, virtual cell, virtual organ, virtual human, the goal is that we can kind of like reduce this time, improve, uh, reduce this timeline.

[330.92s] And, uh, and also we're looking at the entire timeline. Let's say if we only look at like research and development, the models like, you know, protein design and stuff, we might like save like, you know, few years here, but at the end maybe it's not gonna help, uh, for the entire pipeline.

[347.32s] So it's important to have innovation and a breakthrough, uh, across all pipeline.

[356.86s] Now that we know single cell is im-important, how can we measure single cell? So look-looking at single, yeah, it's amazing. This is just one single cell. There is a lot going on inside that one little tiny organism.

[372.10s] Uh, there are different modalities, and each modality is measure different things. Uh, from, um, genome, which is like, you know, DNA sequence and is almost, you know, same for all cells, to RNA sequence.

[385.64s] RNA sequence or transcriptomic is, like, the profile of the genes that they are expressed, uh, at each time and then it, it's like a matrix. And then basically cell- it says for each cell, uh, what are the genes, what are the genes, how many genes are expressed, and then in which quantity.

[404.00s] And is like 20,000. It's, it's 20,000 scale.

[411.30s] And, uh, the other, uh, maybe modality is proteomics. Proteomics maybe is, like, what maybe we care about more, like, because the proteins are the one that they're doing most of the functions in our body.

[423.76s] But the problem is that proteomics is, uh, very hard to measure and, you know, there are ways to measure it, but it's very low, uh, throughput. And morphology is about, like, the, uh, cell shape and structure, and there are, like, really good imaging technologies to kind of also measure, uh, to have, like, microscopic imaging from single cell.

[444.24s] And, um, it's very a- also useful for a spatial, a spatial, uh, dimension, kind of like, you know, knowing the, uh, place of, like, you know, how, where a single cell is located within tissue.

[459.54s] Um, so from all these modalities, maybe the one that has been used mostly for foundation model training, I would say, is RNA-seq. And the reason is that that the technology is, uh, eas- it's easier to measure, and the technology is like b- because of, like, PC, uh, PCR technologies and stuff, it's easier to scale.

[479.28s] So we have, like, usually dataset for single-cell RNA in the scale of, like, tens of mil- tens of, uh, millions of cells to even, like, you know, I've heard 500 million cells and then kind of, like, even, like, there is a project, one billion cells.

[493.82s] But usually what they talk about is, uh, RNA-seq. And then also, this is also a problem that if you really wanna understand biology and then starting from single cell, we really need to kind of have technological advances in other dimensions as well.

[510.54s] And now having said that, let's say we got, like, you know, gathered 1 billion RNA-seq, 1 billion cells, 1 billion samples of RNA-seq ta- data. Is this good for foundation models that we can, you know, train on?

[523.91s] And then the t- the problem is, uh, um, it's, it's very hard. The nature of the data is if you measure two identical cell at the, uh, they don't read the same.

[534.92s] And then the problem is, uh, the problem is this is very, uh, very heterogeneous. Uh, I'll give you, give an example here that usually cells, they are living organism.

[545.84s] They go through a lot of changes and cycles, like, from, like, you know, growing to, uh, kind of copying RNA to cell division. And, uh, usually some of these changes happens, like, in a burst, not like ...

[561.32s] It's not something, you know, continuous. And what we are measuring with current, uh, single-cell sequencing is like a snapshot. We're taking a snapshots, uh, from, from a whole movie.

[576.66s] Uh, now with that, and then also there is the biological reason that the data is very noisy, it's very heterogeneous. Also, there is, like, technical reasons that usually if you measure in different labs, different machines also, the data would be- the data wouldn't be the same.

[594.10s] Now let's see how, what are ... look at some of the foundation models that we have and then see what we- they're doing with this, uh, data. Mm. And then also, like, uh, maybe a small note here that given the nature of data that is very high-dimensional, it's, like, multi-state.

[610.54s] I think maybe, you know, some might argue that, uh, uh, quantum computing would be the, like, kind of like natural fit for this application. And then, yeah, we don't know, it might be true.

[621.52s] Uh, but, you know, until we have quantum compute, for now we wanna see what we can get, uh, with current state-of-the-art AI.

[630.52s] And now, uh, I wanna start with, like, transformer-based models, and there are been- they've been really good, like, you know, papers and models out there from the community. So starting from, like, scGPT and Geneformer.

[643.94s] Uh, and what they want, they kind of like treat each, uh, cell like a sentence and, um, genes like tokens. So basically se- cell are built from genes. And what they do is, like, uh, uh, the, mm, like, you know, BERT st- a BERT-style model, like, from language that kind of, uh, masking

[669.58s] some of the genes and the trying ... having the model to predict that, uh, them, pr- predict that genes, uh, that gene counts. So looking at the data is like a matrix, uh, and then for each cell, we have like, you know, we have, uh, the count of, uh, each genes.

[688.90s] How many genes are, you know, how many genes are active, uh, per cell. And then it's trying to mask this to, like, um, attention, bidirectional attention across, and then kind of understand the relationship between, you know, between these genes.

[705.76s] And, uh, this is how it's trained. And then, like, there are some, uh, uh, some, some, some downstream tasks that this model is used to. Uh, one is for, uh, so, like, you know, predicting cell type, kind of predicting, um, also, mm, perturbation response modeling.

[726.66s] Uh, but overall, when we look into these models, what they try to do, they try to kind of get the single-cell data and then compress it in a kind of a latent vector and then do either decoding for, like, generative task or, like, classification for, uh, classif- for other task.

[746.16s] And then what happens is when you, uh, compress this data, we're losing a lot of information. It doesn't preserve the, uh, it doesn't preserve the information. And then that's why when we're looking into this model, like, um, uh, these models, we see that sometimes, n- sometimes, like, uh, maybe, uh, s- uh, simple linear models are on par

[769.28s] or, like, sometimes even outperforming this, uh, these, uh, models that, you know, it's like, you know, complex models with a lot of compute. It's been used to train those.

[780.18s] And then also we had, like, two papers last year at NeurIPS. We did, like, co- comprehensive benchmarking on, uh, on these models. One is, uh, multimodal data for, like, imaging and RNA-seq, and the other one is for perturbation response modeling.

[797.64s] So I have the links at the end of my talk. Uh, go ahead and check them out. But, like, the final, the results, uh, the, uh, what we found out was the same, uh, that also is known in the community that even though these models are very expensive to train, uh, at the end they're not performing, uh,

[817.44s] as well comparing to, you know, other domain language, uh, and, and imaging.

[824.14s] And this is our newer, um ... And then so transformer-based also we have, like, flow matching based models, uh, that, uh, you, you start to try to, uh, predict the distribution of the data and, uh, starting from, like, you know, Gaussian noise and then trying to, to match their distribution.

[843.66s] And we have, uh, this paper, uh, we have this model Prime Flow, uh, that is available on arXiv, and it seems that these models, they seem to do better.

[856.27s] There is a better comparing to trans- autoregressive based models, um, because it's tries to kind of match the distribution, predict the distribution rather than kind of, you know, understanding the da- uh, understanding the data and compressing it into, into a, uh, into, into a, a latent vector.

[879.00s] Mm, and this is like, uh, some of the results that, uh, we have. So on the left, we see like Prime Flow, it's the greens, the green dots are, um, uh, ground truth label, and then we see that Prime Flow is kind of trying to match the distribution, whereas other models like CPAD are autoencoder-based.

[899.62s] It's kind of like just mapping to the-- It's trying to predict the mean rather than understanding, understanding the distribution. And then we have like MMD score at the bottom.

[911.76s] Uh, so yeah, that was, uh, uh, my talk. Three, uh, things to take away from this talk is that single cell is important, uh, and it's important to understand this.

[922.70s] Uh, it has application for cellular rejuvenation. It's a path to like digital human, and they're helping with drug development cycle. Uh, then also we looked at, uh, uh, other-- the different modalities to measure from single cell.

[938.56s] RNA sequence data is the one that maybe it's we have it more available in scale, and also it's measuring something important, gene expression profile. But at the same, uh, at the same time that we would like to kind of get more data, work on the scale, but it's important that to work on quality of the data of

[957.80s] the way that we are measuring this data to be a bit more realistic of the real, uh, organism than, uh, than, than just like, you know, scale the data the way it is.

[969.08s] And then my final, uh, conclusion is that for now it seems flow matching models, they're doing better, uh, for single-cell data, trying to match, uh, to the distribution, uh, and, uh, also to be able to, uh, scale these models, uh, that, you know, they can also do well on the data they haven't seen, they haven't trained on.

[991.08s] We would need, you know, massive scaling, scaling of the data, I would say, and then also the quality and the way that we measure data.

[999.02s] And then with that, yeah, we have like three papers, scGeneScope, PerturBench, last year in NeurIPS and then Prime Flow. Uh, check them out and, yeah, let me know if you have any questions.

[1008.78s] Thank you.
