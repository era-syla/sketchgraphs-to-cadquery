import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.021, 0.048).threePointArc((0.02001, 0.04834), (0.019, 0.0486)).lineTo(0.01508, 0.057).lineTo(0.0133, 0.057).lineTo(0.0133, 0.048).lineTo(0.021, 0.048).close()
solid=wp_sketch0.add(loop0).extrude(0.022042239664180573)
