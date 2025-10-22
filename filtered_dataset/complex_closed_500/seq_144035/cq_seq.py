import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0189, 0.0211).lineTo(-0.0551, 0.0211).threePointArc((-0.05722, 0.02022), (-0.0581, 0.0181)).lineTo(-0.0581, -0.0181).threePointArc((-0.05722, -0.02022), (-0.0551, -0.0211)).lineTo(-0.0189, -0.0211).threePointArc((-0.01678, -0.02022), (-0.0159, -0.0181)).lineTo(-0.0159, 0.0181).threePointArc((-0.01678, 0.02022), (-0.0189, 0.0211)).close()
solid=wp_sketch0.add(loop0).extrude(-0.01265029475566408)
