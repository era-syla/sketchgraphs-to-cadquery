import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.22345, -0.10625).lineTo(-0.22345, -0.10625).lineTo(-0.22345, 0.10625).lineTo(0.22345, 0.10625).lineTo(0.22345, -0.10625).close()
solid=wp_sketch0.add(loop0).extrude(1.004628421491671)
