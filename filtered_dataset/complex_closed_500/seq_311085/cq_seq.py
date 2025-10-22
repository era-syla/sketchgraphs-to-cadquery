import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(2.4, 1.7).lineTo(-2.4, 1.7).lineTo(-2.4, -1.7).lineTo(-0.47, -1.7).lineTo(-0.47, -1.58).lineTo(-0.0, -1.58).lineTo(-0.0, -1.7).lineTo(2.4, -1.7).lineTo(2.4, 1.7).close()
solid=wp_sketch0.add(loop0).extrude(-8.579752115634285)
