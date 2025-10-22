import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03156, 0.0187).lineTo(-0.03184, 0.0187).lineTo(-0.03184, -0.01909).lineTo(0.03156, -0.01909).lineTo(0.03156, 0.0187).close()
solid=wp_sketch0.add(loop0).extrude(0.0032765258258415347)
