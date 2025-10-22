import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-2.39633, -1.33174).lineTo(2.40367, -1.33174).lineTo(2.40367, 10.96826).lineTo(-2.39633, 10.96826).lineTo(-2.39633, -1.33174).close()
solid=wp_sketch0.add(loop0).extrude(-7.652309760634092)
