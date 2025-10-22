import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(1.13669, 0.36463).lineTo(0.88007, 0.36463).lineTo(0.88007, 0.22497).lineTo(1.13669, 0.22497).lineTo(1.13669, 0.36463).close()
solid=wp_sketch0.add(loop0).extrude(-0.22229806723955442)
