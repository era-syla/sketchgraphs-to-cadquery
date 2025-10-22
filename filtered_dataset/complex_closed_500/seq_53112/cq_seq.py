import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.127, -0.03937).threePointArc((0.12383, -0.04255), (0.127, -0.04572)).lineTo(0.13018, -0.04572).lineTo(0.13018, -0.0489).lineTo(0.127, -0.0489).threePointArc((0.12065, -0.04255), (0.127, -0.0362)).lineTo(0.13018, -0.0362).lineTo(0.13018, -0.03937).lineTo(0.127, -0.03937).close()
solid=wp_sketch0.add(loop0).extrude(0.02318444205731407)
