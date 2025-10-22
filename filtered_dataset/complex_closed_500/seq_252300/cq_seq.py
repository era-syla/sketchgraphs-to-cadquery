import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0375, 0.0668).lineTo(-0.0375, -0.0668).threePointArc((-0.03432, -0.07447), (-0.02665, -0.07765)).lineTo(0.02665, -0.07765).threePointArc((0.03432, -0.07447), (0.0375, -0.0668)).lineTo(0.0375, 0.0668).threePointArc((0.03432, 0.07447), (0.02665, 0.07765)).lineTo(-0.02665, 0.07765).threePointArc((-0.03432, 0.07447), (-0.0375, 0.0668)).close()
solid=wp_sketch0.add(loop0).extrude(0.10578897251193381)
