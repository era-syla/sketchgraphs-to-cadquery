import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.044, 0.026).threePointArc((-0.04824, 0.02424), (-0.05, 0.02)).lineTo(-0.05, -0.02).threePointArc((-0.04824, -0.02424), (-0.044, -0.026)).lineTo(0.044, -0.026).threePointArc((0.04824, -0.02424), (0.05, -0.02)).lineTo(0.05, 0.02).threePointArc((0.04824, 0.02424), (0.044, 0.026)).lineTo(-0.044, 0.026).close()
solid=wp_sketch0.add(loop0).extrude(-0.16864618029294504)
