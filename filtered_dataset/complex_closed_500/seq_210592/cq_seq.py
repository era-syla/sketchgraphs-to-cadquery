import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07186, 0.07401).lineTo(0.0703, 0.07401).lineTo(0.0703, -0.0783).lineTo(-0.07186, -0.0783).lineTo(-0.07186, 0.07401).close()
solid=wp_sketch0.add(loop0).extrude(-0.03649198934426387)
