import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.08513, 0.12801).lineTo(0.06949, 0.10479).lineTo(0.07787, 0.10098).lineTo(0.08513, 0.12801).close()
solid=wp_sketch0.add(loop0).extrude(0.03693062784619827)
