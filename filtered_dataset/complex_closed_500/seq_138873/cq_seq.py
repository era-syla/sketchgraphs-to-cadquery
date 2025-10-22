import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04208, 0.02683).lineTo(-0.03608, 0.02683).lineTo(-0.03608, 0.0194).lineTo(-0.00108, 0.0194).threePointArc((0.01388, 0.00908), (0.02884, 0.0194)).lineTo(0.06384, 0.0194).lineTo(0.06384, 0.02683).lineTo(0.06984, 0.02683).lineTo(0.06984, 0.0114).lineTo(0.02884, 0.0114).threePointArc((0.01388, 0.00308), (-0.00108, 0.0114)).lineTo(-0.03608, 0.0114).lineTo(-0.04208, 0.0114).lineTo(-0.04208, 0.02683).close()
solid=wp_sketch0.add(loop0).extrude(-0.18990352701907282)
