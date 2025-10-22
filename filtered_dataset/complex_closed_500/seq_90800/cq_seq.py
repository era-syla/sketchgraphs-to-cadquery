import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.2, -0.15).lineTo(0.05, -0.15).lineTo(0.05, -0.138).lineTo(0.2, -0.138).lineTo(0.2, -0.15).close()
solid=wp_sketch0.add(loop0).extrude(0.14458906943871266)
