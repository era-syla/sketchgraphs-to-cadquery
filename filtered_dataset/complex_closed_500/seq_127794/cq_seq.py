import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00102, -0.00064).lineTo(-0.00102, -0.00064).lineTo(-0.00102, 0.00063).lineTo(0.00102, 0.00063).lineTo(0.00102, -0.00064).close()
solid=wp_sketch0.add(loop0).extrude(0.005559880304657291)
