import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05159, 0.0363).lineTo(0.00356, 0.0363).lineTo(0.00356, -0.01494).lineTo(-0.05159, -0.01494).lineTo(-0.05159, 0.0363).close()
solid=wp_sketch0.add(loop0).extrude(-0.028727164488795285)
