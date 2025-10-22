import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.05147, 0.03996).lineTo(-0.05147, 0.03996).lineTo(-0.05147, -0.03996).lineTo(0.05147, -0.03996).lineTo(0.05147, 0.03996).close()
solid=wp_sketch0.add(loop0).extrude(-0.03390593383225506)
