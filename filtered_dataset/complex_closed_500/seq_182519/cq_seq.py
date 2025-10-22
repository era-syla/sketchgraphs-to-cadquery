import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01803, 0.00914).lineTo(-0.00102, 0.00914).lineTo(-0.00102, 0.00102).lineTo(-0.01803, 0.00102).lineTo(-0.01803, 0.00914).close()
solid=wp_sketch0.add(loop0).extrude(0.01663751787288163)
