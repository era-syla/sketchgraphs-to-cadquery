import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07014, 0.05).lineTo(0.12986, 0.05).lineTo(0.12986, -0.05).lineTo(-0.07014, -0.05).lineTo(-0.07014, 0.05).close()
solid=wp_sketch0.add(loop0).extrude(-0.05156334785876188)
