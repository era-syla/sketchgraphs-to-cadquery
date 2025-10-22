import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09525, 0.4572).lineTo(0.09525, 0.4572).lineTo(0.09525, -0.4572).lineTo(-0.09525, -0.4572).lineTo(-0.09525, 0.4572).close()
solid=wp_sketch0.add(loop0).extrude(1.5524673571597098)
