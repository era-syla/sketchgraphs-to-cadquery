import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.13473, 0.0491).lineTo(0.11527, 0.0491).lineTo(0.11527, -0.0309).lineTo(-0.13473, -0.0309).lineTo(-0.13473, 0.0491).close()
solid=wp_sketch0.add(loop0).extrude(0.04978655011937427)
