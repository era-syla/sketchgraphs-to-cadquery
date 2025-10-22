import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06986, -0.06876).lineTo(-0.06986, -0.06876).lineTo(-0.06986, 0.06876).lineTo(0.06986, 0.06876).lineTo(0.06986, -0.06876).close()
solid=wp_sketch0.add(loop0).extrude(-0.30104767653254844)
