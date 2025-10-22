import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02393, 0.12141).lineTo(-0.01651, 0.12185).lineTo(-0.01652, 0.12035).lineTo(0.02392, 0.11991).lineTo(0.02393, 0.12141).close()
solid=wp_sketch0.add(loop0).extrude(-0.10632359804976069)
