import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0259, 0.07).lineTo(0.0259, 0.07).lineTo(0.0259, 0.08814).lineTo(-0.0259, 0.08814).lineTo(-0.0259, 0.07).close()
solid=wp_sketch0.add(loop0).extrude(-0.05771632631538019)
