import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.019).lineTo(-0.006, -0.019).lineTo(-0.006, -0.031).lineTo(0.006, -0.031).lineTo(0.006, -0.019).lineTo(0.0, -0.019).close()
solid=wp_sketch0.add(loop0).extrude(0.018522420334858822)
