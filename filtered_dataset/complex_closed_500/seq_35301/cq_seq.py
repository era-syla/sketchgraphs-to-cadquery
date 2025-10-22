import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03175, -0.0381).lineTo(0.03175, -0.0381).threePointArc((0.03624, -0.03624), (0.0381, -0.03175)).lineTo(0.0381, 0.03175).threePointArc((0.03624, 0.03624), (0.03175, 0.0381)).lineTo(-0.03175, 0.0381).threePointArc((-0.03624, 0.03624), (-0.0381, 0.03175)).lineTo(-0.0381, -0.03175).threePointArc((-0.03624, -0.03624), (-0.03175, -0.0381)).close()
solid=wp_sketch0.add(loop0).extrude(-0.15082027440438833)
