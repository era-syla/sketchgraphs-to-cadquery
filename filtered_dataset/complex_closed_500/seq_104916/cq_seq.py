import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02618, 0.0455).lineTo(-0.01382, 0.0455).lineTo(-0.01382, 0.0425).lineTo(0.02618, 0.0425).lineTo(0.02618, 0.0455).close()
solid=wp_sketch0.add(loop0).extrude(0.07817008826058491)
