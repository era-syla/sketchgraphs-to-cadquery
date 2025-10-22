import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02, 1.71871).lineTo(-0.01995, 1.71871).lineTo(-0.01995, 1.7287).lineTo(0.02, 1.7287).lineTo(0.02, 1.71871).close()
solid=wp_sketch0.add(loop0).extrude(0.07665193397249459)
