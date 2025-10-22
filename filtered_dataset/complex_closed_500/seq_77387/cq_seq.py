import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00018, 0.11866).lineTo(0.07094, 0.11866).lineTo(0.07094, 0.10361).lineTo(-0.00018, 0.10361).lineTo(-0.00018, 0.11866).close()
solid=wp_sketch0.add(loop0).extrude(-0.11181490893116611)
