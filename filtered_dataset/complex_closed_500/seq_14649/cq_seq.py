import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07085, 0.06988).lineTo(-0.06356, 0.06988).lineTo(-0.06356, 0.06161).lineTo(-0.07085, 0.06161).lineTo(-0.07085, 0.06988).close()
solid=wp_sketch0.add(loop0).extrude(-0.01604309960701383)
