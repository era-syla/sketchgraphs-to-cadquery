import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.08986, 0.05208).lineTo(0.0955, 0.05208).lineTo(0.0955, -0.05335).lineTo(-0.08986, -0.05335).lineTo(-0.08986, 0.05208).close()
solid=wp_sketch0.add(loop0).extrude(0.29727601683599364)
