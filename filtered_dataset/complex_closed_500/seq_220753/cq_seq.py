import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.29942, 2.26229).lineTo(-0.81818, 2.26229).lineTo(-0.81818, 2.71949).lineTo(0.29942, 2.71949).lineTo(0.29942, 2.26229).close()
solid=wp_sketch0.add(loop0).extrude(-2.619067971310351)
