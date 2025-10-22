import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05, 0.017).lineTo(0.08, 0.017).lineTo(0.08, 0.03121).lineTo(0.05561, 0.05561).lineTo(0.03439, 0.03439).lineTo(0.05, 0.01879).lineTo(0.05, 0.017).close()
solid=wp_sketch0.add(loop0).extrude(-0.05874040923429288)
