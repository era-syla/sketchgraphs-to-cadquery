import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09423, 0.07387).lineTo(0.07495, 0.07387).lineTo(0.07495, -0.1629).lineTo(-0.09423, -0.1629).lineTo(-0.09423, 0.07387).close()
solid=wp_sketch0.add(loop0).extrude(-0.6254614967918427)
