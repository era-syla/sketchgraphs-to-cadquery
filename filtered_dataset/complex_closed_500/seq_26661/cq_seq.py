import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0067, 0.00743).lineTo(0.00562, 0.0084).lineTo(-0.00779, -0.00647).lineTo(-0.00531, -0.00871).lineTo(0.00809, 0.00614).lineTo(0.0067, 0.00743).close()
solid=wp_sketch0.add(loop0).extrude(-0.0052452778954711335)
