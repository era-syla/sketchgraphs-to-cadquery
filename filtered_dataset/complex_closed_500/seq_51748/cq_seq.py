import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0185, 0.0).lineTo(0.0185, 0.015).lineTo(0.01275, 0.015).lineTo(0.01275, 0.025).lineTo(0.0105, 0.025).lineTo(0.0105, 0.031).lineTo(0.01275, 0.031).lineTo(0.01275, 0.0365).lineTo(0.0, 0.0365).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.08463559679925015)
