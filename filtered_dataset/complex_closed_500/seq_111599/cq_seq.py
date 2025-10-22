import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(7.25032, 0.35437).lineTo(7.24445, 0.35437).lineTo(7.24445, -0.425).lineTo(7.25032, -0.425).lineTo(7.25032, 0.35437).close()
solid=wp_sketch0.add(loop0).extrude(1.3868094040235253)
