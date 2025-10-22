import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.7112, -5.4356).lineTo(0.4826, -5.4356).lineTo(0.4826, -5.0546).lineTo(0.7112, -5.0546).lineTo(0.7112, -5.4356).close()
solid=wp_sketch0.add(loop0).extrude(0.4130297270868103)
