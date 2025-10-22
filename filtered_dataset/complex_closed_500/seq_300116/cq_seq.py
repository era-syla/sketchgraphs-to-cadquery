import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.29986, -0.075).lineTo(0.33986, -0.075).lineTo(0.33986, -0.069).lineTo(0.29986, -0.069).lineTo(0.29986, -0.075).close()
solid=wp_sketch0.add(loop0).extrude(-0.06376767126024789)
