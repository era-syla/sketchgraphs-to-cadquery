import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05, 0.0181).lineTo(-0.05, -0.0181).threePointArc((-0.04813, -0.02342), (-0.04334, -0.0264)).threePointArc((-0.0, -0.03115), (0.04334, -0.0264)).threePointArc((0.04813, -0.02342), (0.05, -0.0181)).lineTo(0.05, 0.0181).threePointArc((0.04813, 0.02342), (0.04334, 0.0264)).threePointArc((0.0, 0.03115), (-0.04334, 0.0264)).threePointArc((-0.04813, 0.02342), (-0.05, 0.0181)).close()
solid=wp_sketch0.add(loop0).extrude(-0.0437334055497088)
