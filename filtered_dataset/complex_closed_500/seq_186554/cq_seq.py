import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.002, 0.04232).lineTo(0.0359, 0.04232).lineTo(0.0359, 0.04377).lineTo(0.002, 0.04377).lineTo(0.002, 0.04232).close()
solid=wp_sketch0.add(loop0).extrude(-0.04589888718148307)
