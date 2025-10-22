import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00051, -0.03304).lineTo(-0.00051, -0.03304).lineTo(-0.00051, -0.01677).lineTo(0.00051, -0.01677).lineTo(0.00051, -0.03304).close()
solid=wp_sketch0.add(loop0).extrude(-0.01483069357780575)
