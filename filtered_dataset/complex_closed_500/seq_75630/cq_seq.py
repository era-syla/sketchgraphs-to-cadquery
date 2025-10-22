import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.119, 0.094).lineTo(-0.119, 0.094).lineTo(-0.119, -0.094).lineTo(0.119, -0.094).lineTo(0.119, 0.094).close()
solid=wp_sketch0.add(loop0).extrude(-0.21593687700593925)
