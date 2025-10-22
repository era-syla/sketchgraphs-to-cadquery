import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00765, 0.02).lineTo(-0.00765, 0.02).lineTo(-0.00765, -0.02).lineTo(0.00765, -0.02).lineTo(0.00765, 0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.009750840384909658)
