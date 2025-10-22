import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04013, -0.00559).threePointArc((0.0, 0.00914), (-0.04013, -0.00559)).lineTo(-0.03584, -0.00867).threePointArc((-0.03514, -0.00902), (-0.03436, -0.00914)).lineTo(0.03436, -0.00914).threePointArc((0.03514, -0.00902), (0.03584, -0.00867)).lineTo(0.04013, -0.00559).close()
solid=wp_sketch0.add(loop0).extrude(0.221438721369615)
