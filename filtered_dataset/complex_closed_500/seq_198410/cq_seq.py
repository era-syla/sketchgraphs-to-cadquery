import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00078, 0.00585).lineTo(-0.00078, -0.00453).lineTo(0.00215, -0.01087).lineTo(0.00562, -0.01087).lineTo(0.00589, 0.01083).lineTo(0.00045, 0.01131).lineTo(0.00137, 0.00734).lineTo(-0.00078, 0.00585).close()
solid=wp_sketch0.add(loop0).extrude(0.060443109312023006)
