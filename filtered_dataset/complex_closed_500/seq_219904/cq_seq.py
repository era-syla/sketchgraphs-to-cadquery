import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.8796, -1.23331).lineTo(1.9812, -1.23331).lineTo(1.9812, -1.18251).lineTo(1.8796, -1.18251).lineTo(1.8796, -1.23331).close()
solid=wp_sketch0.add(loop0).extrude(0.002400378474526753)
